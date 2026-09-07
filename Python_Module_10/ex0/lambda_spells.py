def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
    ]
    spells = ["fireball", "heal", "shield"]
    # mages = [
    #     {'name': 'Wizard', 'power': 40, 'element': 'fire'},
    #     {'name': 'Electro-Wizard', 'power': 90, 'element': 'electricity'},
    #     {'name': 'Ice-WIzard', 'power': 65, 'element': 'ice'},
    # ]

    print("\nTesting artifact sorter...")
    sorter = artifact_sorter(artifacts)
    print(
        f"{sorter[0]['name']} ({sorter[0]['power']} power) comes"
        f" before {sorter[1]['name']} ({sorter[1]['power']} power)\n"
    )

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    # print("\nTesting power filter...")
    # for mage in power_filter(mages, 50):
    #     print(f"{mage['name']} ({mage['power']} power)")
    # print()

    # print("Testing mage stats...")
    # stats = mage_stats(mages)
    # print(f"Min power {stats['min_power']}")
    # print(f"MAx power {stats['max_power']}")
    # print(f"Average {stats['avg_power']}")


if __name__ == "__main__":
    main()
