import operator
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def base_enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment of power {power} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast_spell.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    # print(f"Min: {spell_reducer(spells, 'min')}")
    # print(f"Empty list: {spell_reducer([], 'add')}")

    # print()
    # print("Testing partial enchanter...")
    # enchanters = partial_enchanter(base_enchant)
    # print(enchanters["fire"]("Sword"))
    # print(enchanters["ice"]("Shield"))
    # print(enchanters["lightning"]("Staff"))

    print()
    print("Testing memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    # print(memoized_fibonacci.cache_info())

    print()
    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(f"Damage spell: {cast(42)}")
    print(cast("fireball"))
    print(cast(["a", "b", "c"]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
