package main

import "fmt"


class Backpack:

    def __init__(self, size):
        pass

    def get_contents(self):
        pass

    def get_counts(self):
        pass

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def most_popular(self):
        pass


// backpack structure
type backpack struct {
    size    int
}
 
// Method with a receiver
// of author type
func (a author) show() {
 
    fmt.Println("Author's Name: ", a.name)
    fmt.Println("Branch Name: ", a.branch)
    fmt.Println("Published articles: ", a.particles)
    fmt.Println("Salary: ", a.salary)
}

func main() {
	fmt.Println("Hello, world.")
}