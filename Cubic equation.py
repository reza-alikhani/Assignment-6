import cmath

def solve_cubic(a, b, c, d):
    if a == 0:
        raise ValueError("Coefficient 'a' must not be 0 for a cubic equation.")
    
    
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    
  
    discriminant = (q**2) / 4 + (p**3) / 27
    
   
    if discriminant > 0:
       
        u = cmath.sqrt((q**2) / 4 + (p**3) / 27)
        v = -q / 2 + u
        w = -q / 2 - u
        v_cube_root = cmath.exp(cmath.log(v) / 3) if v != 0 else 0
        w_cube_root = cmath.exp(cmath.log(w) / 3) if w != 0 else 0
        t1 = v_cube_root + w_cube_root
        t2 = -(v_cube_root + w_cube_root) / 2 + (v_cube_root - w_cube_root) * cmath.sqrt(3) * 1j / 2
        t3 = -(v_cube_root + w_cube_root) / 2 - (v_cube_root - w_cube_root) * cmath.sqrt(3) * 1j / 2
    elif discriminant == 0:
       
        u = cmath.sqrt((q**2) / 4 + (p**3) / 27)
        v = -q / 2 + u
        v_cube_root = cmath.exp(cmath.log(v) / 3) if v != 0 else 0
        t1 = 2 * v_cube_root
        t2 = -v_cube_root
        t3 = -v_cube_root
    else:
        
        u = cmath.sqrt((q**2) / 4 + (p**3) / 27)
        v = -q / 2 + u
        w = -q / 2 - u
        v_cube_root = cmath.exp(cmath.log(v) / 3) if v != 0 else 0
        w_cube_root = cmath.exp(cmath.log(w) / 3) if w != 0 else 0
        t1 = v_cube_root + w_cube_root
        t2 = -(v_cube_root + w_cube_root) / 2 + (v_cube_root - w_cube_root) * cmath.sqrt(3) * 1j / 2
        t3 = -(v_cube_root + w_cube_root) / 2 - (v_cube_root - w_cube_root) * cmath.sqrt(3) * 1j / 2
    
    
    x1 = t1 - b / (3*a)
    x2 = t2 - b / (3*a)
    x3 = t3 - b / (3*a)
    
    return (x1, x2, x3)

def main():
    print("Enter the coefficients for the cubic equation ax^3 + bx^2 + cx + d = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))

    try:
        roots = solve_cubic(a, b, c, d)
        print(f"The roots of the cubic equation are: {roots}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
