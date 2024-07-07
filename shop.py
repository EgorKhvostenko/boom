import tkinter as tk
from tkinter import messagebox
class shop:
    def __init__(self, q):
        self.q = q
        self.q.title = 'shop'
        self.q.geometry = ('300x400')

        self.items = [
            {'name':'apple','price':50},
            {'name':'orange','price':60},
            {'name':'milk','price':100}
]
