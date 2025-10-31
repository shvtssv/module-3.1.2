def main():
	print("Калькулятор — 'q' выход, 'h' история на любом шаге")

	history = []

	left = None

	while True:
		try:
			if left is None:
				left_str = input("Введите первое число: ").strip()
				if left_str.lower() == "q":
					return
				if left_str.lower() == "h":
					if not history:
						print("(история пуста)")
					else:
						start = max(1, len(history) - 9)
						for i, item in enumerate(history[-10:], start=start):
							print(f"{i}: {item}")
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


