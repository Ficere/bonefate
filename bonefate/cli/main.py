def main():
    from bonefate import BoneFates
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument("--year", type=int, required=True, help="年份")
    parser.add_argument("--month", type=int, required=True, help="月份")
    parser.add_argument("--day", type=int, required=True, help="日期")
    parser.add_argument("--hour", type=str, required=True, help="时辰")
    parser.add_argument("--lunar", type=bool, default=False, help="是否农历")
    args = parser.parse_args()
    
    bonefate = BoneFates(args.year, args.month, args.day, args.hour, args.lunar)
    print(f"阳历: {bonefate.solar.toString()}")
    print(f"农历: {bonefate.lunar.toFullString()}")
    print(f"称骨: {bonefate.bone_weight}")
    print(f"称骨命书: {bonefate.poem}")
    
if __name__ == "__main__":
    main()