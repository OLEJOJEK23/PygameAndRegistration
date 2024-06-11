import flet as ft
from flet import *
from hashlib import sha256


def main(page: ft.Page) -> None:
    page.title = 'Авторизация'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False

    # Создаем поля

    text_login_signup: TextField = TextField(label='Логин', text_align=ft.TextAlign.LEFT, width=200)
    text_password_signup: TextField = TextField(label='Пароль', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_show_password: Checkbox = Checkbox(label='Я согласен', value=False)
    button_submit_signup: ElevatedButton = ElevatedButton(text='Войти', width=200, disabled=True)
    button_submit_signin: ElevatedButton = ElevatedButton(text='Зарегистрироваться', width=200, disabled=True)
    registration_link: TextButton = TextButton(text='У меня нет аккаунта', width=200)
    text_login_signin: TextField = TextField(label='Логин', text_align=ft.TextAlign.LEFT, width=200)
    text_password_signin: TextField = TextField(label='Пароль', text_align=ft.TextAlign.LEFT, width=200, password=False)
    text_username: TextField = TextField(label='Имя пользователя', text_align=ft.TextAlign.LEFT, width=200)
    text_user_surname: TextField = TextField(label='Фамилия пользователя', text_align=ft.TextAlign.LEFT, width=200)
    login_link:  TextButton = TextButton(text='Войти в существующий аккаунт', width=200)
    dlg = ft.AlertDialog(title=ft.Text("Аккаунт успешно создан"))
    switch_theme = IconButton(icon='dark_mode',selected_icon='light_mode' )

    def show_password(e: ControlEvent) -> None:
        if text_password_signup.password:
            text_password_signup.password = False
            page.update()
        else:
            text_password_signup.password = True
            page.update()

    def check_theme(e: ControlEvent) -> None:
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()

    def validate_login(e: ControlEvent) -> None:
        if all([text_login_signup.value, text_password_signup.value]):
            button_submit_signup.disabled = False
        else:
            button_submit_signup.disabled = True
        page.update()

    def submit_login(e: ControlEvent) -> None:
        user_login = text_login_signup.value
        password = text_password_signup.value
        try:
            my_file = open(f"users/{user_login}.txt", "r")
            lines = my_file.readlines()
            right_hash = lines[0].strip()
            password_hash = sha256(password.encode('utf-8')).hexdigest()
            if password_hash == right_hash:
                page.clean()
                page.add(
                    Row(
                        controls=[Text(value='Здравствуйте', size=25)],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                )
            else:
                print("Неверный пароль")
        except Exception as ex:
            print(f"При попытки создания аккаунта произошла ошибка: {ex}")

    def registration_page(e: ControlEvent) -> None:
        page.title = "Регистрация"
        page.clean()
        page.add(
            Column(
                controls=[
                    Row(
                        controls=[
                            Column(
                                [text_username,
                                 text_user_surname,
                                 text_login_signin,
                                 text_password_signin,
                                 button_submit_signin,
                                 login_link]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[switch_theme],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )

                ]
            )

        )

    def show_login_page(e: ControlEvent) -> None:
        page.title = "Авторизация"
        page.clean()
        page.add(
            Column(
                controls=[
                    Row(
                        controls=[
                            Column(
                                [text_login_signup,
                                 text_password_signup,
                                 checkbox_show_password,
                                 button_submit_signup,
                                 registration_link]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[switch_theme],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )

                ]
            )

        )

    def registration_validation(e: ControlEvent) -> None:
        if all([text_username.value, text_user_surname.value, text_login_signin.value, text_password_signin.value]):
            button_submit_signin.disabled = False
        else:
            button_submit_signin.disabled = True
        page.update()

    def submit_registration(e: ControlEvent) -> None:
        password = text_password_signin.value
        user_login = text_login_signin.value
        username = text_username.value
        user_surname = text_user_surname.value
        try:
            password_hash = sha256(password.encode('utf-8')).hexdigest()
            my_file = open(f"users\{user_login}.txt", "w+")
            my_file.write(f"{password_hash}\n{username}\n{user_surname}")
        except Exception as ex:
            print(f"При попытки создания аккаунта произошла ошибка: {ex}")
        dlg.open = True
        page.update()

    text_login_signup.on_change = validate_login
    text_password_signup.on_change = validate_login
    button_submit_signup.on_click = submit_login
    registration_link.on_click = registration_page
    text_username.on_change = registration_validation
    text_user_surname.on_change = registration_validation
    text_login_signin.on_change = registration_validation
    text_password_signin.on_change = registration_validation
    button_submit_signin.on_click = submit_registration
    login_link.on_click = show_login_page
    checkbox_show_password.on_change = show_password
    switch_theme.on_click = check_theme
    # Добавление элементов на страницу

    page.add(
        Column(
            controls=[
                Row(
                    controls=[
                        Column(
                            [text_login_signup,
                             text_password_signup,
                             checkbox_show_password,
                             button_submit_signup,
                             registration_link]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[switch_theme],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )

            ]
        )

    )


if __name__ == '__main__':
    ft.app(target=main)