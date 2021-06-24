

import numpy as np
import torch


class CONV():
    def __init__(self, in_channel, out_channel, kernel=3, padding=1, stride=1, padding_mode=None):
        self.stride = stride
        self.padding = padding
        self.kernel = kernel
        self.in_channel = in_channel
        self.out_channel = out_channel

        self.w = np.random.standard_normal((in_channel, out_channel, kernel, kernel))
        # self.b = np.random.standard_normal((out_channel))

    def forward(self, x):
        out_size_w, out_size_h = x.shape[2] - self.kernel // 2, x.shape[3] - self.kernel // 2
        out = np.zeros((x.shape[0], x.shape[1], out_size_w, out_size_h))
        if self.padding is not None and self.padding > 0:
            x = np.pad(x, ((0, 0), (0, 0), (self.padding, self.padding), (self.padding, self.padding)))
        for i in range(out_size_h):
            for j in range(out_size_w):
                for in_c in range(self.in_channel):
                    for out_c in range(self.out_channel):
                        t = x[:, in_c: in_c + 1, i:i + self.kernel, j: j + self.kernel]
                        print(t.shape)
                        # torch.bmm()

                        out[:, out_c, i, j] += torch.sum(t)
        return out


x = np.random.standard_normal((1, 3, 10, 10))
conv = CONV(5, 10)
y = conv.forward(x)
