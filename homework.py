from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE: str = ('Тип тренировки: {training_type}; '
                    'Длительность: {duration:.3f} ч.; '
                    'Дистанция: {distance:.3f} км; '
                    'Ср. скорость: {speed:.3f} км/ч; '
                    'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        """Вывод результатов тренировки."""
        return self.MESSAGE.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""

    action: int
    duration: float
    weight: float
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Вы забыли переопределить метод '
                                  f'{type(self).__name__}')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    COEFF_RUNNING_CALORIE_1: int = 18
    COEFF_RUNNING_CALORIE_2: int = 20

    def get_spent_calories(self) -> float:
        return ((self.COEFF_RUNNING_CALORIE_1 * self.get_mean_speed()
                - self.COEFF_RUNNING_CALORIE_2)
                * self.weight / self.M_IN_KM * self.duration
                * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    height: float
    COEFF_WEIGHT_1: float = 0.035
    COEFF_WEIGHT_2: float = 0.029
    EXPONENT: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.COEFF_WEIGHT_1 * self.weight
                + (self.get_mean_speed()**self.EXPONENT // self.height)
                * self.COEFF_WEIGHT_2 * self.weight) * self.duration
                * self.MIN_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""

    length_pool: float
    count_pool: float
    LEN_STEP: ClassVar[float] = 1.38
    COEFF_SWIMING_CALORIE_1: float = 1.1
    COEFF_SWIMING_CALORIE_2: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.get_mean_speed() + self.COEFF_SWIMING_CALORIE_1)
                * self.COEFF_SWIMING_CALORIE_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    types_of_training: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in types_of_training:
        raise ValueError('Данный тип тренировки фитнес-трекер '
                         'не поддерживает')
    return types_of_training[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        main(read_package(workout_type, data))
