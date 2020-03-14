fn main() {
    let x: i8 = -5;
    println!("x = {}", x);
    let x: u8 = 6;
    println!("x = {}", x);

    let x: i16 = -20;
    println!("x = {}", x);
    let x: u16 = 50;
    println!("x = {}", x);

    let x: i32 = 1024;
    println!("x = {}", x);
    let x: u32 = 2048;
    println!("x = {}", x);

    let x: i64 = 2;
    println!("x = {}", x);
    let x: u64 = 33;
    println!("x = {}", x);

    let x: i128 = -88_888;
    println!("x = {}", x);
    let x: u128 = 54;
    println!("x = {}", x);

    let x: f32 = 5.32;
    println!("x = {}", x);

    let x: f64 = 5583.22383;
    println!("x = {}", x);

    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;

    // remainder
    let remainder = 43 % 5;

    // chars, use single quote '
    let c = 'c';
    let z: char = 'z';

    // booleans 
    let b: bool = true;

    // Compounds
    // tuples
    let tup: (i32, f64, char, bool) = (1285, 55.983, 'c', false);
    let mut tup2: (i32, f64, char, bool) = (1285, 55.983, 'c', false);
    tup2 = (112, 33.64, 'a', false);
    
    // Indiviudal access
    tup2.3 = true;
    println!("tup2.3 = {}", tup2.3);
    
    // Extract elements
    let (t1, t2, t3, t4) = tup;
    let b: bool = tup.3;
}
