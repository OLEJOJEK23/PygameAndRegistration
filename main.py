import flet as ft
from src.Inteface import authorization
from src.Game import start_game


if __name__ == '__main__':
    ft.app(target=authorization)
    start_game()