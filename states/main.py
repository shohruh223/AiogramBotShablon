from aiogram.fsm.state import StatesGroup, State


class GetUsernameState(StatesGroup):
    confirm = State()


class TarjimonUzState(StatesGroup):
    confirm = State()

class TarjimonEnState(StatesGroup):
    confirm = State()

class QRCodeState(StatesGroup):
    data = State()
    confirm = State()


class remove_bg(StatesGroup):
    data = State()
    confirm = State()


class my1(StatesGroup):
    data = State()
    confirm = State()