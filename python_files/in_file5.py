from collections import Counter

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

data = datasets.load_iris()

X = np.array(data["data"])
y = np.array(data["target"])
classes = data["target_names"]

X_train, X_test, y_train, y_test = train_test_split(X, y)


def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


def classifier(train_data, train_target, classes, point, k=5):
    data = zip(train_data, train_target)
    # List of distances of all points from the point to be classified
    distances = []
    for data_point in data:
        distance = euclidean_distance(data_point[0], point)
        distances.append((distance, data_point[1]))
    # Choosing 'k' points with the least distances.
    votes = [i[1] for i in sorted(distances)[:k]]
    # Most commonly occurring class among them
    # is the class into which the point is classified
    result = Counter(votes).most_common(1)[0][0]
    return classes[result]


if __name__ == "__main__":
    print(classifier(X_train, y_train, classes, [4.4, 3.1, 1.3, 1.4]))
    

# Make a training dataset drawn from a gaussian distribution
def gaussian_distribution(mean: float, std_dev: float, instance_count: int) -> list:

    seed(1)
    return [gauss(mean, std_dev) for _ in range(instance_count)]


# Make corresponding Y flags to detecting classes
def y_generator(class_count: int, instance_count: list) -> list:

    return [k for k in range(class_count) for _ in range(instance_count[k])]


# Calculate the class means
def calculate_mean(instance_count: int, items: list) -> float:
  
    # the sum of all items divided by number of instances
    return sum(items) / instance_count


# Calculate the class probabilities
def calculate_probabilities(instance_count: int, total_count: int) -> float:
  
    # number of instances in specific class divided by number of all instances
    return instance_count / total_count


# Calculate the variance
def calculate_variance(items: list, means: list, total_count: int) -> float:
  
    squared_diff = []  # An empty list to store all squared differences
    # iterate over number of elements in items
    for i in range(len(items)):
        # for loop iterates over number of elements in inner layer of items
        for j in range(len(items[i])):
            # appending squared differences to 'squared_diff' list
            squared_diff.append((items[i][j] - means[i]) ** 2)

    # one divided by (the number of all instances - number of classes) multiplied by
    # sum of all squared differences
    n_classes = len(means)  # Number of classes in dataset
    return 1 / (total_count - n_classes) * sum(squared_diff)


# Making predictions
def predict_y_values(
    x_items: list, means: list, variance: float, probabilities: list
) -> list:
     
    # An empty list to store generated discriminant values of all items in dataset for
    # each class
    results = []
    # for loop iterates over number of elements in list
    for i in range(len(x_items)):
        # for loop iterates over number of inner items of each element
        for j in range(len(x_items[i])):
            temp = []  # to store all discriminant values of each item as a list
            # for loop iterates over number of classes we have in our dataset
            for k in range(len(x_items)):
                # appending values of discriminants for each class to 'temp' list
                temp.append(
                    x_items[i][j] * (means[k] / variance)
                    - (means[k] ** 2 / (2 * variance))
                    + log(probabilities[k])
                )
            # appending discriminant values of each item to 'results' list
            results.append(temp)

    return [result.index(max(result)) for result in results]


# Calculating Accuracy
def accuracy(actual_y: list, predicted_y: list) -> float:
    # iterate over one element of each list at a time (zip mode)
    # prediction is correct if actual Y value equals to predicted Y value
    correct = sum(1 for i, j in zip(actual_y, predicted_y) if i == j)
    # percentage of accuracy equals to number of correct predictions divided by number
    # of all data and multiplied by 100
    return (correct / len(actual_y)) * 100


num = TypeVar("num")


def valid_input(
    input_type: Callable[[object], num],  # Usually float or int
    input_msg: str,
    err_msg: str,
    condition: Callable[[num], bool] = lambda x: True,
    default: str | None = None,
) -> num:
    while True:
        try:
            user_input = input_type(input(input_msg).strip() or default)
            if condition(user_input):
                return user_input
            else:
                print(f"{user_input}: {err_msg}")
                continue
        except ValueError:
            print(
                f"{user_input}: Incorrect input type, expected {input_type.__name__!r}"
            )


# Main Function
def main():
    """This function starts execution phase"""
    while True:
        print(" Linear Discriminant Analysis ".center(50, "*"))
        print("*" * 50, "\n")
        print("First of all we should specify the number of classes that")
        print("we want to generate as training dataset")
        # Trying to get number of classes
        n_classes = valid_input(
            input_type=int,
            condition=lambda x: x > 0,
            input_msg="Enter the number of classes (Data Groupings): ",
            err_msg="Number of classes should be positive!",
        )

        print("-" * 100)

        # Trying to get the value of standard deviation
        std_dev = valid_input(
            input_type=float,
            condition=lambda x: x >= 0,
            input_msg=(
                "Enter the value of standard deviation"
                "(Default value is 1.0 for all classes): "
            ),
            err_msg="Standard deviation should not be negative!",
            default="1.0",
        )

        print("-" * 100)

        # Trying to get number of instances in classes and theirs means to generate
        # dataset
        counts = []  # An empty list to store instance counts of classes in dataset
        for i in range(n_classes):
            user_count = valid_input(
                input_type=int,
                condition=lambda x: x > 0,
                input_msg=(f"Enter The number of instances for class_{i+1}: "),
                err_msg="Number of instances should be positive!",
            )
            counts.append(user_count)
        print("-" * 100)

        # An empty list to store values of user-entered means of classes
        user_means = []
        for a in range(n_classes):
            user_mean = valid_input(
                input_type=float,
                input_msg=(f"Enter the value of mean for class_{a+1}: "),
                err_msg="This is an invalid value.",
            )
            user_means.append(user_mean)
        print("-" * 100)

        print("Standard deviation: ", std_dev)
        # print out the number of instances in classes in separated line
        for i, count in enumerate(counts, 1):
            print(f"Number of instances in class_{i} is: {count}")
        print("-" * 100)

        # print out mean values of classes separated line
        for i, user_mean in enumerate(user_means, 1):
            print(f"Mean of class_{i} is: {user_mean}")
        print("-" * 100)

        # Generating training dataset drawn from gaussian distribution
        x = [
            gaussian_distribution(user_means[j], std_dev, counts[j])
            for j in range(n_classes)
        ]
        print("Generated Normal Distribution: \n", x)
        print("-" * 100)

        # Generating Ys to detecting corresponding classes
        y = y_generator(n_classes, counts)
        print("Generated Corresponding Ys: \n", y)
        print("-" * 100)

        # Calculating the value of actual mean for each class
        actual_means = [calculate_mean(counts[k], x[k]) for k in range(n_classes)]
        # for loop iterates over number of elements in 'actual_means' list and print
        # out them in separated line
        for i, actual_mean in enumerate(actual_means, 1):
            print(f"Actual(Real) mean of class_{i} is: {actual_mean}")
        print("-" * 100)

        # Calculating the value of probabilities for each class
        probabilities = [
            calculate_probabilities(counts[i], sum(counts)) for i in range(n_classes)
        ]

        # for loop iterates over number of elements in 'probabilities' list and print
        # out them in separated line
        for i, probability in enumerate(probabilities, 1):
            print(f"Probability of class_{i} is: {probability}")
        print("-" * 100)

        # Calculating the values of variance for each class
        variance = calculate_variance(x, actual_means, sum(counts))
        print("Variance: ", variance)
        print("-" * 100)

        # Predicting Y values
        # storing predicted Y values in 'pre_indexes' variable
        pre_indexes = predict_y_values(x, actual_means, variance, probabilities)
        print("-" * 100)

        # Calculating Accuracy of the model
        print(f"Accuracy: {accuracy(y, pre_indexes)}")
        print("-" * 100)
        print(" DONE ".center(100, "+"))

        if input("Press any key to restart or 'q' for quit: ").strip().lower() == "q":
            print("\n" + "GoodBye!".center(100, "-") + "\n")
            break
        system("cls" if name == "nt" else "clear")  # noqa: S605


if __name__ == "__main__":
    main()