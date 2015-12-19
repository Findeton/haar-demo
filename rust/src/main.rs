use std::collections::VecDeque;
use std::io::{self, Write};

fn haar_level(f: Vec<f64>) -> (Vec<f64>, Vec<f64>){
    let mut a: Vec<f64> = Vec::new();
    let mut d: Vec<f64> = Vec::new();
    let base : f64 = 1.0f64 / 2.0f64.powf(0.5f64); 
    let n : usize = f.len() / 2;
    for i in 0..n {
        a.push(base*(f[2*i] + f[2*i+1]));
        d.push(base*(f[2*i] - f[2*i+1]));
    }
    (a, d)
}

fn haar(f: Vec<f64>) -> VecDeque<Vec<f64>> {
    let n = (f.len() as f64).log2().trunc() as u32;
    println!("n {}", n);
    let mut a: Vec<f64> = Vec::new();
    let m = 2u32.pow(n) as usize;
    for i in 0..m {
        a.push(f[i]);
    }
    let mut res : VecDeque<Vec<f64>> = VecDeque::new();
    while a.len() > 1 {
        let (newa, d) = haar_level(a);
        a = newa;
        res.push_front(d);
    }
    res.push_front(a);
    res
}

fn inverse_haar_level(a: Vec<f64>, d: Vec<f64>) -> Vec<f64> {
    let base : f64 = 1.0f64 / 2.0f64.powf(0.5f64); 
    let mut res : Vec<f64> = Vec::new();
    for i in 0..a.len() {
        res.push(base*(a[i] + d[i]));
        res.push(base*(a[i] - d[i]));
    }
    res
}

fn inverse_haar(h: VecDeque<Vec<f64>>) -> Vec<f64> {
    let mut an = h[0].clone();
    for i in 1..h.len() {
        an = inverse_haar_level( an, h[i].clone() );
    }
    an
}

fn print(d : Vec<f64>, end: bool)
{
    print!("[ ");
    for  i in &d {
        print!("{}, ", i);
    }
    
    print!(" ] ");
    if end {
     print!("\n");
    }
    
    io::stdout().flush().unwrap();
    
}

fn print2(d : VecDeque<Vec<f64>>)
{
    print!("[ ");
    for  i in d {
        print(i, false);
    }
    print!(" ]\n");
    
    io::stdout().flush().unwrap();
    
}

fn main() {
    let data : Vec<f64> = vec![4.,6.,10.,12.,8.,6.,5.,5.];
    print(data.clone(), true);
    let res = haar(data);
    print2(res.clone());
    print(inverse_haar(res.clone()), true);
}
