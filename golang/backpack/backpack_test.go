package backpack_test

import (
	"backpack/backpack"
	"github.com/davecgh/go-spew/spew"
	"testing"
)

func stringSlicesEqual(a, b []string) bool {
	if len(a) != len(b) {
		spew.Dump(a)
		spew.Dump(b)
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

func TestBackpack_GetMaxSize(t *testing.T) {
	b := backpack.NewBackpack(backpack.Parameters{})
	size := b.GetMaxSize()
	if size != 10 {
		t.Errorf("Default was = %d; want 10", size)
	}

	b = backpack.NewBackpack(backpack.Parameters{Size: 11})
	size = b.GetMaxSize()
	if size != 11 {
		t.Errorf("Default was = %d; want 11", size)
	}
}

func TestBackpack_GetContents(t *testing.T) {
	b := backpack.NewBackpack(backpack.Parameters{})
	contents := b.GetContents()
	defaultContents := []string{}
	contentsEqual := stringSlicesEqual(contents, defaultContents)
	if contentsEqual == false {
		t.Errorf("Default contents was = %s; want %s", contents, defaultContents)
	}
}

func TestBackpack_Add(t *testing.T) {
	b := backpack.NewBackpack(backpack.Parameters{})
	b.Add("ax")
	contents := b.GetContents()

	contentsEqual := stringSlicesEqual(contents, []string{"ax"})
	if contentsEqual == false {
		t.Errorf("Contents was = %s; want [ax]", contents)
	}

}
