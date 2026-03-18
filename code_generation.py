import time
import random
import pyautogui
import keyboard  # To listen to key presses

def human_typing(text, speed_factor=0.4):
    """ Simulates human-like typing """
    
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, speed_factor))

def main():
    code = """


import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        assert embed_dim % num_heads == 0
        self.head_dim = embed_dim // num_heads
        self.num_heads = num_heads
        self.scale = self.head_dim ** -0.5

        self.qkv = nn.Linear(embed_dim, embed_dim * 3)
        self.out = nn.Linear(embed_dim, embed_dim)

    def forward(self, x, mask=None, kv=None):
        B, T, C = x.size()
        if kv is None:
            kv = x
        qkv = self.qkv(torch.cat([x, kv, kv], dim=-1) if kv is not None else x)
        q, k, v = qkv.chunk(3, dim=-1)

        q = q.view(B, T, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(B, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(B, -1, self.num_heads, self.head_dim).transpose(1, 2)

        attn = (q @ k.transpose(-2, -1)) * self.scale
        if mask is not None:
            attn = attn.masked_fill(mask == 0, float('-inf'))
        attn = attn.softmax(dim=-1)

        out = attn @ v
        out = out.transpose(1, 2).contiguous().view(B, T, C)
        return self.out(out)

class FeedForward(nn.Module):
    def __init__(self, embed_dim, ff_dim, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(ff_dim, embed_dim)
        )

    def forward(self, x):
        return self.net(x)

class TransformerBlock(nn.Module):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.1):
        super().__init__()
        self.attn = MultiHeadAttention(embed_dim, num_heads)
        self.ff = FeedForward(embed_dim, ff_dim, dropout)
        self.ln1 = nn.LayerNorm(embed_dim)
        self.ln2 = nn.LayerNorm(embed_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None, kv=None):
        x = x + self.dropout(self.attn(self.ln1(x), mask, kv))
        x = x + self.dropout(self.ff(self.ln2(x)))
        return x

class PositionalEncoding(nn.Module):
    def __init__(self, embed_dim, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, embed_dim)
        pos = torch.arange(0, max_len).unsqueeze(1)
        div = torch.exp(torch.arange(0, embed_dim, 2) * (-math.log(10000.0) / embed_dim))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]

class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, depth, num_heads, ff_dim, max_len=512):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.pos = PositionalEncoding(embed_dim, max_len)
        self.blocks = nn.Sequential(*[
            TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(depth)
        ])
        self.ln = nn.LayerNorm(embed_dim)

    def forward(self, x, mask=None):
        x = self.embed(x)
        x = self.pos(x)
        return self.ln(self.blocks(x, mask))

class TransformerDecoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, depth, num_heads, ff_dim, max_len=512):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.pos = PositionalEncoding(embed_dim, max_len)
        self.blocks = nn.ModuleList([
            TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(depth)
        ])
        self.ln = nn.LayerNorm(embed_dim)
        self.fc_out = nn.Linear(embed_dim, vocab_size)

    def forward(self, x, enc_out, src_mask=None, tgt_mask=None):
        x = self.embed(x)
        x = self.pos(x)
        for block in self.blocks:
            x = block(x, tgt_mask, kv=enc_out)
        x = self.ln(x)
        return self.fc_out(x)

class Transformer(nn.Module):
    def __init__(self, src_vocab, tgt_vocab, embed_dim=512, depth=6, heads=8, ff_dim=2048, max_len=512):
        super().__init__()
        self.encoder = TransformerEncoder(src_vocab, embed_dim, depth, heads, ff_dim, max_len)
        self.decoder = TransformerDecoder(tgt_vocab, embed_dim, depth, heads, ff_dim, max_len)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        enc_out = self.encoder(src, src_mask)
        return self.decoder(tgt, enc_out, src_mask, tgt_mask)



    """  # The text to be typed continuously
    stop_key_count = 0  # To track the "9" key presses
    
    print("Press '9' twice to stop the script.")
    
    # Continuous loop to keep retyping the code indefinitely
    while True:
        # Check if the "9" key has been pressed twice
        if keyboard.is_pressed('9'):
            stop_key_count += 1
            print(f"Key '9' pressed. Count: {stop_key_count}")
            time.sleep(0.5)  # Prevent counting the key press multiple times in quick succession
            
            if stop_key_count == 2:
                print("Pressed '9' twice. Stopping the script.")
                break  # Exit the loop
        
        # Delay before starting the typing
        time.sleep(5)  # This gives you 5 seconds to focus on the text field or application
        
        print("Typing code...\n")
        human_typing(code)

if __name__ == "__main__":
    main()
