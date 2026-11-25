class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []

        for p, s in cars:
            time = (target - p) / s
            if not fleets or time > fleets[-1]:   # slower than the fleet ahead → new fleet
                fleets.append(time)
    # else: catches up → merges, do nothing

        return len(fleets)