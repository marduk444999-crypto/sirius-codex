import hashlib
import random
import json

def hex_to_digits(hex_str):
    """
    Преобразует HEX строку в массив цифр (0-9)
    """
    return [int(c, 16) % 10 for c in hex_str]

def generate_cube(payload):
    """
    Генерирует 3D-куб 9x9x9 из JSON, используя SHA-256 и случайные цифры для заполнения.
    """
    payload_str = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    h = hashlib.sha256(payload_str.encode()).hexdigest()
    digits = hex_to_digits(h)
    cube = [[[0 for x in range(9)] for y in range(9)] for z in range(9)]
    idx = 0
    for z in range(9):
        for y in range(9):
            for x in range(9):
                if idx < len(digits):
                    cube[z][y][x] = digits[idx]
                else:
                    cube[z][y][x] = random.randint(0,9)
                idx += 1
    return cube

if __name__ == '__main__':
    # Пример полезной нагрузки: замените на свои параметры!
    payload = {
        "CAR_ID": "CAT-001",
        "route_id": "R-8848-ALPHA",
        "timestamp": 1710864000,
        "nonce": "a1b2c3d4"
    }
    cube = generate_cube(payload)

    # Выводим первую проекцию (TOP) для проверки
    print("TOP-грань (cube[0]):")
    for row in cube[0]:
        print(row)

    # Можно добавить сохранение куба в файл или вывод всех граней
    # Например, сохранить в JSON:
    with open("codexcube.json", "w", encoding="utf-8") as f:
        json.dump(cube, f, ensure_ascii=False)
    print("Куб успешно сгенерирован и сохранён в codexcube.json.")
