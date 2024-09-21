import math

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

def entropy(y):
    total_count = len(y)
    label_counts = {}
    for label in y:
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1

    entropy_value = 0.0
    for label in label_counts:
        proportion = label_counts[label] / total_count
        entropy_value -= proportion * math.log2(proportion)
    
    return entropy_value

def split(X, y, feature, threshold):
    left_X, left_y, right_X, right_y = [], [], [], []
    
    for i in range(len(X)):
        if X[i][feature] <= threshold:
            left_X.append(X[i])
            left_y.append(y[i])
        else:
            right_X.append(X[i])
            right_y.append(y[i])
    
    return left_X, right_X, left_y, right_y

def information_gain(y, y_left, y_right):
    weight_left = len(y_left) / len(y)
    weight_right = len(y_right) / len(y)
    return entropy(y) - (weight_left * entropy(y_left) + weight_right * entropy(y_right))

def best_split(X, y):
    best_gain = -1
    split_feature = None
    split_threshold = None

    num_features = len(X[0])
    for feature in range(num_features):
        thresholds = set([x[feature] for x in X])
        for threshold in thresholds:
            left_X, right_X, left_y, right_y = split(X, y, feature, threshold)

            if len(left_y) == 0 or len(right_y) == 0:
                continue

            gain = information_gain(y, left_y, right_y)

            if gain > best_gain:
                best_gain = gain
                split_feature = feature
                split_threshold = threshold

    return split_feature, split_threshold

def build_tree(X, y, depth=0, max_depth=5):
    if len(set(y)) == 1 or depth == max_depth:
        leaf_value = max(set(y), key=y.count)
        return Node(value=leaf_value)

    feature, threshold = best_split(X, y)

    if feature is None:
        leaf_value = max(set(y), key=y.count)
        return Node(value=leaf_value)

    left_X, right_X, left_y, right_y = split(X, y, feature, threshold)

    left_subtree = build_tree(left_X, left_y, depth + 1, max_depth)
    right_subtree = build_tree(right_X, right_y, depth + 1, max_depth)

    return Node(feature=feature, threshold=threshold, left=left_subtree, right=right_subtree)

def predict_tree(node, X):
    if node.value is not None:
        return node.value

    if X[node.feature] <= node.threshold:
        return predict_tree(node.left, X)
    else:
        return predict_tree(node.right, X)

def predict(X, tree):
    return [predict_tree(tree, x) for x in X]

# Example usage
if __name__ == "__main__":
    X = [[2, 3], [10, 15], [3, 6], [9, 12], [4, 7]]
    y = [0, 1, 0, 1, 0]

    tree = build_tree(X, y)
    predictions = predict(X, tree)
    print("Predictions:", predictions)
