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
	var numOfUsers, numOfRequests int
	fmt.Fscan(in, &numOfUsers, &numOfRequests)
	notifications := make(map[int]int)
	requestNumber := 0
	for i := 0; i < numOfRequests; i++ {
		var requestType string
		var userId int
		fmt.Fscan(in, &requestType, &userId)
		if requestType == "1" {
			requestNumber++
			notifications[userId] = requestNumber
		} else {
			fmt.Fprintln(out, max(notifications[userId], notifications[0]))
		}
	}
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
