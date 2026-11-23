import math

def trigonometric_operations():
    angle = 30

    radian = math.radians(angle)

    print("Angle:", angle, "degrees")

    print("Sin:", math.sin(radian))
    print("Cos:", math.cos(radian))
    print("Tan:", math.tan(radian))

    print("Sin inverse:", math.degrees(math.asin(math.sin(radian))))
    print("Cos inverse:", math.degrees(math.acos(math.cos(radian))))
    print("Tan inverse:", math.degrees(math.atan(math.tan(radian))))

trigonometric_operations()
