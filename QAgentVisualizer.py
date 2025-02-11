import argparse
from tkinter import TOP, Button, Canvas, Tk

import numpy as np


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Q-Learning Visualization with customizable parameters"
    )
    parser.add_argument(
        "--size", type=int, default=6, help="Size of the grid (default: 6)"
    )
    parser.add_argument(
        "--reward",
        type=float,
        default=100,
        help="Reward value for reaching the goal (default: 100)",
    )
    parser.add_argument(
        "--gain", type=float, default=0.5, help="Learning rate/gain (default: 0.5)"
    )
    return parser.parse_args()


class QAgentVisualizer:
    def __init__(self, size=6, reward=100, gain=0.5):
        self.window = Tk()
        self.window.title("Q-Learning")
        self.size = size
        self.size_of_square = 60
        self.reward = reward
        self.gain = gain
        self.posX = 0
        self.posY = 0
        self.Q = np.zeros((np.square(size), 4))
        self.rewardMatrix = np.zeros((np.square(size), 1))
        self.rewardMatrix[np.square(size) - 1] = self.reward
        self.stop = False
        self.block_square = np.zeros(np.square(size))
        self.canvas = Canvas(
            self.window,
            height=self.size_of_square * self.size,
            width=self.size_of_square * self.size,
            background="white",
        )

    def create_window(self):
        for j in range(self.size):
            for i in range(self.size):
                self.canvas.create_rectangle(
                    i * self.size_of_square,
                    j * self.size_of_square,
                    (i + 1) * self.size_of_square,
                    (j + 1) * self.size_of_square,
                    fill="white",
                )

        self.canvas.create_rectangle(
            0, 0, self.size_of_square, self.size_of_square, fill="red"
        )

        button_start = Button(self.window, text="Start", command=self.moveSquare)
        button_start.pack(side=TOP, padx=5, pady=5)

        button__stop = Button(self.window, text="Stop", command=self.stopSquare)
        button__stop.pack(side=TOP, padx=5, pady=5)

        self.canvas.bind("<Button-1>", self.createBlockSquare)
        self.canvas.pack()
        self.window.mainloop()

    def moveSquare(self):
        if (
            self.Q[0, 0] == 0
            and self.Q[0, 1] == 0
            and self.Q[0, 2] == 0
            and self.Q[0, 3] == 0
        ):

            if not (self.posX == self.size - 1 and self.posY == self.size - 1):

                if (
                    self.Q[self.posY * self.size + self.posX, 0] == 0
                    and self.Q[self.posY * self.size + self.posX, 1] == 0
                    and self.Q[self.posY * self.size + self.posX, 2] == 0
                    and self.Q[self.posY * self.size + self.posX, 3] == 0
                ):

                    direction = np.round(np.random.randint(4))

                    # going UP
                    if direction == 0:

                        if (
                            self.posY != 0
                            and self.block_square[
                                (self.posY - 1) * self.size + self.posX
                            ]
                            != -1
                        ):

                            posYnew = self.posY - 1

                            self.canvas.create_rectangle(
                                self.posX * self.size_of_square,
                                self.posY * self.size_of_square,
                                (self.posX + 1) * self.size_of_square,
                                (self.posY + 1) * self.size_of_square,
                                fill="white",
                            )

                            self.Q[self.posY * self.size + self.posX, 0] = (
                                self.rewardMatrix[
                                    posYnew * self.size + self.posX
                                ].item()
                                + self.gain
                                * np.max(
                                    self.Q[posYnew * self.size + self.posX, :]
                                ).item()
                            )

                            if self.Q[self.posY * self.size + self.posX, 0] != 0:
                                self.canvas.create_rectangle(
                                    self.posX * self.size_of_square,
                                    posYnew * self.size_of_square,
                                    (self.posX + 1) * self.size_of_square,
                                    (posYnew + 1) * self.size_of_square,
                                    fill="blue",
                                )
                            else:
                                self.canvas.create_rectangle(
                                    self.posX * self.size_of_square,
                                    posYnew * self.size_of_square,
                                    (self.posX + 1) * self.size_of_square,
                                    (posYnew + 1) * self.size_of_square,
                                    fill="red",
                                )
                            self.posY = posYnew

                    # going RIGHT
                    elif direction == 1:

                        if (
                            self.posX != self.size - 1
                            and self.block_square[
                                self.posY * self.size + (self.posX + 1)
                            ]
                            != -1
                        ):
                            posXnew = self.posX + 1

                            self.canvas.create_rectangle(
                                self.posX * self.size_of_square,
                                self.posY * self.size_of_square,
                                (self.posX + 1) * self.size_of_square,
                                (self.posY + 1) * self.size_of_square,
                                fill="white",
                            )

                            self.Q[self.posY * self.size + self.posX, 1] = (
                                self.rewardMatrix[
                                    self.posY * self.size + posXnew
                                ].item()
                                + self.gain
                                * np.max(
                                    self.Q[self.posY * self.size + posXnew, :]
                                ).item()
                            )

                            if self.Q[self.posY * self.size + self.posX, 1] != 0:
                                self.canvas.create_rectangle(
                                    posXnew * self.size_of_square,
                                    self.posY * self.size_of_square,
                                    (posXnew + 1) * self.size_of_square,
                                    (self.posY + 1) * self.size_of_square,
                                    fill="blue",
                                )
                            else:
                                self.canvas.create_rectangle(
                                    posXnew * self.size_of_square,
                                    self.posY * self.size_of_square,
                                    (posXnew + 1) * self.size_of_square,
                                    (self.posY + 1) * self.size_of_square,
                                    fill="red",
                                )

                            self.posX = posXnew

                    # going DOWN
                    elif direction == 2:

                        if (
                            self.posY != self.size - 1
                            and self.block_square[
                                (self.posY + 1) * self.size + self.posX
                            ]
                            != -1
                        ):

                            posYnew = self.posY + 1

                            self.canvas.create_rectangle(
                                self.posX * self.size_of_square,
                                self.posY * self.size_of_square,
                                (self.posX + 1) * self.size_of_square,
                                (self.posY + 1) * self.size_of_square,
                                fill="white",
                            )

                            self.Q[self.posY * self.size + self.posX, 2] = (
                                self.rewardMatrix[
                                    posYnew * self.size + self.posX
                                ].item()
                                + self.gain
                                * np.max(
                                    self.Q[posYnew * self.size + self.posX, :]
                                ).item()
                            )

                            if self.Q[self.posY * self.size + self.posX, 2] != 0:
                                self.canvas.create_rectangle(
                                    self.posX * self.size_of_square,
                                    posYnew * self.size_of_square,
                                    (self.posX + 1) * self.size_of_square,
                                    (posYnew + 1) * self.size_of_square,
                                    fill="blue",
                                )
                            else:
                                self.canvas.create_rectangle(
                                    self.posX * self.size_of_square,
                                    posYnew * self.size_of_square,
                                    (self.posX + 1) * self.size_of_square,
                                    (posYnew + 1) * self.size_of_square,
                                    fill="red",
                                )

                            self.posY = posYnew

                    # going LEFT
                    elif direction == 3:

                        if (
                            self.posX != 0
                            and self.block_square[
                                self.posY * self.size + (self.posX - 1)
                            ]
                            != -1
                        ):

                            posXnew = self.posX - 1

                            self.canvas.create_rectangle(
                                self.posX * self.size_of_square,
                                self.posY * self.size_of_square,
                                (self.posX + 1) * self.size_of_square,
                                (self.posY + 1) * self.size_of_square,
                                fill="white",
                            )

                            self.Q[self.posY * self.size + self.posX, 3] = (
                                self.rewardMatrix[
                                    self.posY * self.size + posXnew
                                ].item()
                                + self.gain
                                * np.max(
                                    self.Q[self.posY * self.size + posXnew, :]
                                ).item()
                            )

                            if self.Q[self.posY * self.size + self.posX, 3] != 0:
                                self.canvas.create_rectangle(
                                    posXnew * self.size_of_square,
                                    self.posY * self.size_of_square,
                                    (posXnew + 1) * self.size_of_square,
                                    (self.posY + 1) * self.size_of_square,
                                    fill="blue",
                                )
                            else:
                                self.canvas.create_rectangle(
                                    posXnew * self.size_of_square,
                                    self.posY * self.size_of_square,
                                    (posXnew + 1) * self.size_of_square,
                                    (self.posY + 1) * self.size_of_square,
                                    fill="red",
                                )

                            self.posX = posXnew

                else:

                    index = np.argmax(self.Q[self.posY * self.size + self.posX, :])

                    if index == 0:
                        self.posY -= 1

                    if index == 1:
                        self.posX += 1

                    if index == 2:
                        self.posY += 1

                    if index == 3:
                        self.posX -= 1

            else:
                self.posX = 0
                self.posY = 0

        if self.stop == False:
            self.window.after(10, self.moveSquare)
        self.stop = False

    def createBlockSquare(self, event):

        mouse_click_x_position = event.x
        mouse_click_y_position = event.y

        horizontal_square_index = int(mouse_click_x_position / self.size_of_square)
        vertical_square_index = int(mouse_click_y_position / self.size_of_square)

        self.block_square[
            self.size * vertical_square_index + horizontal_square_index
        ] = -1

        self.canvas.create_rectangle(
            horizontal_square_index * self.size_of_square,
            vertical_square_index * self.size_of_square,
            (horizontal_square_index + 1) * self.size_of_square,
            (vertical_square_index + 1) * self.size_of_square,
            fill="black",
        )

    def stopSquare(self):
        self.stop = True


if __name__ == "__main__":
    args = parse_arguments()
    app = QAgentVisualizer(size=args.size, reward=args.reward, gain=args.gain)
    app.create_window()
