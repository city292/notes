# checkpoint
torch.utils.checkpoint.checkpoint(function, *args, **kwargs)
为模型或模型的一部分设置Checkpoint
检查点用计算换内存（节省内存）。 检查点部分并不保存中间激活值，而是在反向传播时重新计算它们。 它可以应用于模型的任何部分。
具体而言，在前向传递中，function将以torch.no_grad（）的方式运行，即不存储中间激活值。 相反，前向传递将保存输入元组和function参数。 在反向传播时，检索保存的输入和function参数，然后再次对函数进行正向计算，现在跟踪中间激活值，然后使用这些激活值计算梯度。

（也即，检查点部分在前向计算时不存储中间量，等反向传播需要计算梯度时重新计算这些中间量）
checkpoint一种用时间换空间的策略
```python
import torch.utils.checkpoint as checkpoint
net = net() # nn.Moudle
if self.use_checkpoint:
    x = checkpoint.checkpoint(net, x, attn_mask)
else:
    x = net(x, attn_mask)
```