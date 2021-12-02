use std::env;
use std::fs;

fn read_input() -> String {
    fs::read_to_string("../inputs/day_01.txt").expect("Something went wrong reading the file.")
}

pub fn run() {
    println!("Day 01");
    let content = read_input();
    println!("Text:\n{}", content); 
}