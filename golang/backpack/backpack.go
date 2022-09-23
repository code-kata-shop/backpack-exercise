package backpack

type Backpack struct {
	contents []string
	maxSize  int
}

type Parameters struct {
	Size int // default is 5
}

func NewBackpack(parameters Parameters) *Backpack {
	b := new(Backpack)
	b.maxSize = 10
	if parameters.Size != 0 {
		b.maxSize = parameters.Size
	}
	b.contents = make([]string, 0)
	return b
}

func (b Backpack) GetContents() []string {
	return b.contents

}

func (b Backpack) GetMaxSize() int {
	return b.maxSize
}

func (b *Backpack) Add(item string) **Backpack {
	b.contents = append(b.contents, item)
	return &b
}

func (b Backpack) Remove(item string) {

}

func (b Backpack) MostPopular() {

}
