package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var numOfSets int
	fmt.Fscan(in, &numOfSets)

	for i := 0; i < numOfSets; i++ {
		var numOfDevs int
		var num string
		skillLevel := make(map[int]int)
		fmt.Fscan(in, &numOfDevs)
		for i := 0; i < numOfDevs; i++ {
			fmt.Fscan(in, &num)
			skillLevel[i], _ = strconv.Atoi(num)
		}
		for i := 0; i < numOfDevs/2; i++ {
			minIndex := getMinIndex(skillLevel)
			firstDev := skillLevel[minIndex]
			delete(skillLevel, minIndex)
			secondDev, _ := getSecondDev(skillLevel, firstDev)
			fmt.Fprintln(out, minIndex+1, secondDev+1)
			delete(skillLevel, secondDev)
		}
		fmt.Fprintln(out)
	}

}

func getSecondDev(values map[int]int, firstDev int) (int, int) {
	minValue := -1
	minIndex := 0
	for k, v := range values {
		absNum := abs(firstDev - v)
		if minValue == -1 || absNum < minValue || absNum == minValue && k < minIndex {
			minIndex = k
			minValue = absNum
		}
	}

	return minIndex, values[minIndex]

}

func getMinIndex(values map[int]int) int {
	minIndex := -1
	for k, _ := range values {
		if minIndex == -1 || minIndex > k {
			minIndex = k
		}
	}

	return minIndex

}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value

}
