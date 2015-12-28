package main

import (
    "fmt"
    "math"
)

func haar_level(f []float64) (a []float64 , d []float64) {
    var base float64 = 1.0 / math.Pow(2, 0.5)
    var n int = len(f) / 2
    for i := 0; i < n; i++ {
        a = append(a, base*(f[2*i] + f[2*i+1]))
        d = append(d, base*(f[2*i] - f[2*i+1]))
    }
    return
}

func haar(f []float64) [][]float64 {
    n := int(math.Log2(float64(len(f))))
    fmt.Println("n ", n)
    m := int(math.Pow(2, float64(n)))
    var A []float64 = f[:m]
    var res [][]float64
    for len(A) > 1 {
        var D []float64
        A, D = haar_level(A)
        res = append([][]float64{D}, res...) // prepend
    }
    res = append([][]float64{A}, res...) // prepend
    return res
}

func inverse_haar_level(a []float64, d []float64) (res []float64) {
    var base float64 = 1.0 / math.Pow(2, 0.5)
    for i:= 0; i < len(a); i++ {
        res = append(res, base*(a[i] + d[i]))
        res = append(res, base*(a[i] - d[i]))
    }
    return
}

func inverse_haar(h [][]float64) (an []float64) {
    an = h[0]
    for i := 1; i < len(h); i++ {
        an = inverse_haar_level(an, h[i])
    }
    return
}

func main() {
    data := []float64{4,6,10,12,8,6,5,5}
    fmt.Println(data)
    res := haar(data)
    fmt.Println(res)
    fmt.Println(inverse_haar(res))
}