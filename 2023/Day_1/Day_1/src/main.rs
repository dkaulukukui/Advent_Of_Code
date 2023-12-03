//use std::env;
use std::fs;


fn main() {
    // --snip--
    
    let file_path = String::from("C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\2023\\Day_1\\input.txt");

    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}