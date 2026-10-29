import 'package:flutter/material.dart';
import 'package:mobile/components/button_component.dart';
import 'package:mobile/components/input_component.dart';
import 'package:mobile/pages/home_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  String username = "";
  String password = "";

  void login() {
    if (username == "" || password == "") {
      // mensagem de erro
    }

    if (username == "admin" && password == "admin") {
      Navigator.of(
        context,
      ).push(MaterialPageRoute<void>(builder: (context) => const HomeScreen()));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center, // Centraliza verticalmente
        crossAxisAlignment:
            CrossAxisAlignment.center, // Centraliza horizontalmente
        children: [
          Container(
            padding: EdgeInsets.all(8),
            child: Column(
              spacing: 15,
              children: [
                InputComponent(
                  label: "username",
                  onChange: (value) => username = value,
                ),
                InputComponent(
                  label: "password",
                  onChange: (value) => password = value,
                ),
                SizedBox(height: 10),
                ButtonComponent(text: "Login", onPressed: login),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
