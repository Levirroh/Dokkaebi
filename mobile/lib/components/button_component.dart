import 'package:flutter/material.dart';
import 'package:mobile/styles/colors.dart';

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
    return TextButton(
      style: TextButton.styleFrom(
        backgroundColor: AppColors.pink,
        alignment: Alignment.center,
        foregroundColor: AppColors.background,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12.0), // Adjust radius value here
        ),
      ),
      onPressed: widget.onPressed,
      child: Text(widget.text),
    );
  }
}
