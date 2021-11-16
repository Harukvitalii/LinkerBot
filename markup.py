from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ---- Menu ------
btnlecMenu = KeyboardButton('🪟Меню')


btnMath = KeyboardButton('🔱Виш мат')
btnIngeniring = KeyboardButton('🎲Інженерія')
btnSport = KeyboardButton('🍫Фіз-вих')
btnGraphics = KeyboardButton('🍕Графіка')
btnImov = KeyboardButton('💹Ймовірність')

btnENG = KeyboardButton('🏳️‍⚧️English')
btnFilosofy = KeyboardButton('💤Філософія')
btnPsico = KeyboardButton('🙉Психологія')

btnback = KeyboardButton('👈👈👈')
# --- english ----
btn1pg = KeyboardButton('😎1 пг')
btn2pg = KeyboardButton('👻2 пг')
btnPractMenu = KeyboardButton('📜Меню')

EnglecMenu = ReplyKeyboardMarkup(resize_keyboard = True).add (btn1pg, btn2pg, btnlecMenu)


EngpractMenu = ReplyKeyboardMarkup(resize_keyboard = True).add (btn1pg, btn2pg, btnPractMenu)


#---- lecMenu ====

lecMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnGraphics, btnImov, btnIngeniring, btnMath, btnSport, btnFilosofy, btnPsico, btnENG, btnback)



#---- practMenu ====
btnImovPract = KeyboardButton('🐻Ймовірність')
btnMathPract = KeyboardButton('✨Виш мат')
btnIngeniringPract = KeyboardButton('🔥Інженерія')


practMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnGraphics, btnImovPract, btnIngeniring, btnMathPract, btnSport, btnFilosofy, btnPsico, btnENG, btnback)



# ---- main Menu

btnLec = KeyboardButton('Лекційний')
btnPract = KeyboardButton('Практичний')


mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLec, btnPract)











