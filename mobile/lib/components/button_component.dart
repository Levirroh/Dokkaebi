import 'package:flutter/material.dart';

class ButtonComponent extends StatefulWidget {
  const ButtonComponent({
    super.key,
    required this.text,
    required this.onPressed,
    this.active = true,
  });

  final bool active;
  final String text;
  final VoidCallback onPressed;

  @override
  State<ButtonComponent> createState() => _ButtonComponentState();
}

class _ButtonComponentState extends State<ButtonComponent> {
  @override
  Widget build(BuildContext context) {
    return TextButton(onPressed: widget.onPressed, child: Text(widget.text));
  }
}
