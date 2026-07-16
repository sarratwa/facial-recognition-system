import sys
import traceback


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    failures = []

    section("1. Python")
    print("Executable:", sys.executable)
    print("Version:", sys.version)

    # TensorFlow
    section("2. TensorFlow")
    try:
        import tensorflow as tf

        print("TensorFlow version:", tf.__version__)
        print("TensorFlow path:", tf.__file__)
        print("Built with CUDA:", tf.test.is_built_with_cuda())

        print("\nVisible physical devices:")
        for device in tf.config.list_physical_devices():
            print(" -", device)

        gpus = tf.config.list_physical_devices("GPU")
        print("\nDetected GPUs:", len(gpus))

        if gpus:
            for gpu in gpus:
                print(" -", gpu)
        else:
            print("No GPU detected. TensorFlow will use the CPU.")

        # Basic tensor operation
        a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        b = tf.constant([[5.0, 6.0], [7.0, 8.0]])
        result = tf.matmul(a, b)

        print("\nMatrix multiplication result:")
        print(result.numpy())

        # Show which device performs the operation
        print("\nDevice used for the tensor result:")
        print(result.device)

    except Exception as error:
        failures.append("TensorFlow")
        print("TensorFlow test FAILED:", error)
        traceback.print_exc()

    # Keras
    section("3. TensorFlow/Keras model")
    try:
        import tensorflow as tf

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(
                4,
                activation="relu",
                input_shape=(3,)
            ),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer="adam", loss="mse")

        x = tf.constant([
            [1.0, 2.0, 3.0],
            [2.0, 3.0, 4.0],
            [3.0, 4.0, 5.0],
            [4.0, 5.0, 6.0]
        ])

        y = tf.constant([
            [1.0],
            [2.0],
            [3.0],
            [4.0]
        ])

        model.fit(x, y, epochs=1, verbose=0)
        prediction = model.predict(x[:1], verbose=0)

        print("Tiny model trained successfully.")
        print("Example prediction:", prediction)

    except Exception as error:
        failures.append("Keras")
        print("Keras test FAILED:", error)
        traceback.print_exc()

    # OpenCV
    section("4. OpenCV")
    try:
        import cv2
        import numpy as np

        print("OpenCV version:", cv2.__version__)

        image = np.zeros((100, 100, 3), dtype=np.uint8)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        print("Created image shape:", image.shape)
        print("Converted grayscale shape:", gray.shape)
        print("OpenCV test passed.")

    except Exception as error:
        failures.append("OpenCV")
        print("OpenCV test FAILED:", error)
        traceback.print_exc()

    # Matplotlib
    section("5. Matplotlib")
    try:
        import matplotlib
        matplotlib.use("Agg")

        import matplotlib.pyplot as plt

        print("Matplotlib version:", matplotlib.__version__)

        plt.figure()
        plt.plot([1, 2, 3], [1, 4, 9])
        plt.title("Dependency test")
        plt.savefig("dependency_test_plot.png")
        plt.close()

        print("Plot created: dependency_test_plot.png")
        print("Matplotlib test passed.")

    except Exception as error:
        failures.append("Matplotlib")
        print("Matplotlib test FAILED:", error)
        traceback.print_exc()

    section("Final result")

    if failures:
        print("Some tests failed:")
        for package in failures:
            print(" -", package)
        sys.exit(1)

    print("All dependency tests passed.")

    if "tf" in locals():
        if tf.config.list_physical_devices("GPU"):
            print("TensorFlow can see your GPU.")
        else:
            print("TensorFlow works, but it cannot currently see a GPU.")


if __name__ == "__main__":
    main()