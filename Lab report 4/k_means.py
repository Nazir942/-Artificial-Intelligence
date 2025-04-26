import random
import csv

class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.group = None

class ModifiedKMeans:
    def __init__(self, num_points, num_clusters):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.grid = [[0 for _ in range(50)] for _ in range(50)]
        self.points = []
        self.centers = []
        self.load_data()
        self.run_clustering()

    def load_data(self):
        with open('data.csv', 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                if row['Type'] == 'Point':
                    self.points.append(DataPoint(int(row['X']), int(row['Y'])))
                elif row['Type'] == 'Center':
                    self.centers.append(DataPoint(int(row['X']), int(row['Y'])))

    def run_clustering(self):
        while True:
            for point in self.points:
                closest_dist = float('inf')
                for idx, center in enumerate(self.centers):
                    distance = abs(point.x - center.x) + abs(point.y - center.y)
                    if distance < closest_dist:
                        closest_dist = distance
                        point.group = idx

            new_centers = [DataPoint(center.x, center.y) for center in self.centers]

            for idx in range(self.num_clusters):
                sum_x = sum_y = count = 0
                for point in self.points:
                    if point.group == idx:
                        sum_x += point.x
                        sum_y += point.y
                        count += 1
                if count > 0:
                    self.centers[idx].x = sum_x // count
                    self.centers[idx].y = sum_y // count

            shift = 0
            for i in range(self.num_clusters):
                shift += abs(self.centers[i].x - new_centers[i].x) + abs(self.centers[i].y - new_centers[i].y)
            if shift == 0:
                break

        for pt in self.points:
            self.grid[pt.x][pt.y] = pt.group + 1
        for cen in self.centers:
            self.grid[cen.x][cen.y] = 'C'

        for idx in range(self.num_clusters):
            intra_distance = sum(
                abs(self.centers[idx].x - pt.x) + abs(self.centers[idx].y - pt.y)
                for pt in self.points if pt.group == idx
            )
            print(f"Cluster {idx + 1} Intra-distance: {intra_distance}")

        for pt in self.points:
            print(f"Point ({pt.x}, {pt.y}) - Cluster {pt.group + 1}")

        for idx, cen in enumerate(self.centers):
            print(f"Cluster {idx + 1} Center at ({cen.x}, {cen.y})")

        print("\nMatrix Visualization:\n")
        for i in range(50):
            for j in range(50):
                if self.grid[i][j] == 0:
                    print('.', end=' ')
                elif self.grid[i][j] == 'C':
                    print('C', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()

def create_data_file(num_points, num_clusters):
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "X", "Y"])
        for _ in range(num_points):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Point", x, y])
        for _ in range(num_clusters):
            x = random.randint(0, 49)
            y = random.randint(0, 49)
            writer.writerow(["Center", x, y])

def main():
    points = 100
    clusters = 10
    create_data_file(points, clusters)
    ModifiedKMeans(points, clusters)

if __name__ == "__main__":
    main()
