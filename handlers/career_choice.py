from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.prof_keyboards import make_row_keyboard


router = Router()

available_prof_names = ["Разработчик", "Аналитик", "Тестировщик"]
available_prof_grades = ["Jun", "Mid", "Senior"]

class ChoiseProfNames(StatesGroup):
    choice_prof_names = State()
    choice_prof_grades = State()

#Хендлер на команду /prof
@router.message(Command('prof'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
        f'Привет, {name}, выбери профессию',
        reply_markup=make_row_keyboard(available_prof_names)
    )
    await state.set_state(ChoiseProfNames.choice_prof_names)


@router.message(ChoiseProfNames.choice_prof_names, F.text.in_(available_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_prof=message.text.lower())
    await message.answer(
        f'Спасибо, Теперь выбери совй уровень',
        reply_markup=make_row_keyboard(available_prof_grades)
    )
    await state.set_state(ChoiseProfNames.choice_prof_grades)

@router.message(ChoiseProfNames.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer(
        f'Я не знаю такой профессии',
        reply_markup=make_row_keyboard(available_prof_names)
    )


