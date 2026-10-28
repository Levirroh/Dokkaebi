import 'package:flutter/material.dart';
import 'package:mobile/components/input_component.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  late String username;
  late String password;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          InputComponent(label: "User", onChange: (value) => username = value),
          InputComponent(
            label: "Password",
            onChange: (value) => password = value,
          ),
          Text("entrar"),
        ],
      ),
    );
  }
}
