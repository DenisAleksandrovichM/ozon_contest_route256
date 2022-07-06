package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var numOfSets int
	fmt.Fscan(in, &numOfSets)
	for i := 0; i < numOfSets; i++ {
		var numOfTasks, task int
		var tasks []int
		completedTasks := make(map[int]bool)
		reportIsCorrect := true
		fmt.Fscan(in, &numOfTasks)
		for i := 0; i < numOfTasks; i++ {
			fmt.Fscan(in, &task)
			tasks = append(tasks, task)
			completedTasks[task] = false
		}
		prevTask := tasks[0]
		completedTasks[prevTask] = true
		for _, value := range tasks {
			if prevTask == value {
				continue
			}
			prevTask = value
			if completedTasks[value] {
				reportIsCorrect = false
			} else {
				completedTasks[value] = true
			}
		}
		if reportIsCorrect {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
