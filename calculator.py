def main(): #запускаем функцию
	print("Калькулятор — 'q' выход, 'h' история на любом шаге")

	history = []  #создали пустой список с именем history, чтобы потом записывать в него все действия.

	left = None  #создали переменную "левое" число, то, которое вводится первым в операции. 
	#None — означает "ничего", "отсутствие значения". мы не знаем, какое число введёт пользователь, поэтому пока кладём в коробку left "ничего".
    #как итог: мы зарезервировали место для первого числа, но пока оно пустое.

	while True: #пока (условие) ИСТИНА, повторяй следующий блок кода. Так как условие True всегда истинно, этот цикл будет повторяться бесконечно.
		#Наш калькулятор будет работать, пока мы сами его не остановим (командой q).
		try: #компьютер, попробуй выполнить весь следующий кусок кода (до except). Если в нём пользователь сделает что-то не так (например, введёт буквы вместо цифр), 
			#возникнет ошибка, НЕ закрывай программу, а перейди сразу к блоку except и выполни то, что там написано".
             #это защита от сбоев. Без try программа бы просто "падала", если ввести не число.
			if left is None:  
				left_str = input("Введите первое число: ").strip() #strip() — означает "обрезать" лишние пробелы в начале и в конце строки
				if left_str.lower() == "q": #.lower() — это метод, который преобразует все буквы в строке в нижний регистр (делает их маленькими).
					                        #Если пользователь ввёл Q или q, left_str.lower() превратит это в q.
					return #завершаем и выходим из калькулятора, потому что до этого мы спросили если q(выйти из калькулятора)
				if left_str.lower() == "h": 
					if not history:
						print("(история пуста)") #если пользователь ввел h а список пуста, то мы так и выводим
					else:
						start = max(1, len(history) - 9) #len(history) — это длина списка (сколько всего записей в истории). 
						for i, item in enumerate(history[-10:], start=start): #возьми последние 10 элементов списка". Если элементов меньше 10, возьми все.
							                                                #enumerate(...) — эта функция нумерует элементы списка. Она возвращает два значения: 
							                                                 #индекс (i) и сам элемент (item).
							print(f"{i}: {item}")    #f-строка. Это способ вставить значения переменных прямо в текст   
					continue
				left = float(left_str)

			op = input("Введите оператор (+ - * / % ^): ").strip()
			if op.lower() == "q":
				return
			if op.lower() == "h":
				if not history:
					print("(история пуста)")
				else:
					start = max(1, len(history) - 9)
					for i, item in enumerate(history[-10:], start=start):
						print(f"{i}: {item}")
				continue

			right_str = input("Введите второе число: ").strip()
			if right_str.lower() == "q":
				return
			if right_str.lower() == "h":
				if not history:
					print("(история пуста)")
				else:
					start = max(1, len(history) - 9)
					for i, item in enumerate(history[-10:], start=start):
						print(f"{i}: {item}")
				continue
			right = float(right_str)

			if op == "+":
				result = left + right
			elif op == "-":
				result = left - right
			elif op == "*":
				result = left * right
			elif op == "/":
				if right == 0:
					print("Ошибка: Деление на ноль недопустимо")
					continue
				result = left / right
			elif op == "%":
				if right == 0:
					print("Ошибка: Остаток по модулю на ноль недопустим")
					continue
				result = left % right
			elif op == "^":
				result = left ** right
			else:
				print("Ошибка: Неподдерживаемый оператор. Используйте + - * / % ^")
				continue

			print(result)
			history.append(f"{left} {op} {right} = {result}")

			while True:
				action = input("(c) продолжить с результатом, (n) новая операция, (q) выход, (h) история: ").strip().lower()
				if action == "h":
					if not history:
						print("(история пуста)")
					else:
						start = max(1, len(history) - 9)
						for i, item in enumerate(history[-10:], start=start):
							print(f"{i}: {item}")
					continue
				if action == "q":
					return
				if action == "n":
					left = None
					break
				if action == "c" or action == "":
					left = result
					break
				print("Введите c, n, q или h")
		except ValueError:
			print("Ошибка: Введите корректные числа")


if __name__ == "__main__":
	main()


