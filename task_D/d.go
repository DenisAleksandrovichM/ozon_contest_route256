package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var numOfPass int
	patterns := map[string]string{
		"upper_letters":     "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
		"lower_letters":     "abcdefghijklmnopqrstuvwxyz",
		"digits":            "1234567890",
		"vowels_letters":    "euioayEUIOAY",
		"consonant_letters": "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ",
	}
	fmt.Fscan(in, &numOfPass)
	for i := 0; i < numOfPass; i++ {
		checkResult := map[string]bool{
			"upper_letters":     false,
			"lower_letters":     false,
			"digits":            false,
			"vowels_letters":    false,
			"consonant_letters": false,
		}
		var password string
		isValid := true
		fmt.Fscan(in, &password)
		for k, v := range patterns {
			checkResult[k] = strings.ContainsAny(v, password)
			if checkResult[k] == false {
				isValid = false
			}
		}

		if isValid {
			fmt.Fprintln(out, password)
			continue
		}

		if !checkResult["digits"] {
			password += "1"
		}

		if !checkResult["upper_letters"] {
			if !checkResult["vowels_letters"] {
				checkResult["vowels_letters"] = true
				password += "E"
			} else {
				checkResult["consonant_letters"] = true
				password += "B"
			}
		}

		if !checkResult["lower_letters"] {
			if !checkResult["vowels_letters"] {
				checkResult["vowels_letters"] = true
				password += "e"
			} else {
				checkResult["consonant_letters"] = true
				password += "b"
			}
		}

		if !checkResult["vowels_letters"] {
			password += "e"
		}
		if !checkResult["consonant_letters"] {
			password += "b"
		}

		fmt.Fprintln(out, password)

	}
}
