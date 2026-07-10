package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", home)
	fmt.Println("Dokkaebi iniciado")
	err := http.ListenAndServe("127.0.0.1:8000", nil)

	if err != nil {
		fmt.Println("Erro ao iniciar servidor", err)
	}
}

func home(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	response := map[string]string{
		"message": "Dokkaebi node está funcionando!",
	}

	json.NewEncoder(w).Encode(response)

}
