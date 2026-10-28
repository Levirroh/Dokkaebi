import 'package:flutter/material.dart';

class InputComponent extends StatefulWidget {
  const InputComponent({
    super.key,
    required this.label,
    required this.onChange,
    this.showHideText = false,
  });

  final bool showHideText;
  final String label;
  final ValueChanged<String> onChange;

  @override
  State<InputComponent> createState() => _InputComponentState();
}

class _InputComponentState extends State<InputComponent> {
  late bool _hideText = widget.showHideText;

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      obscureText: _hideText,
      decoration: InputDecoration(
        labelText: widget.label,
        suffixIcon: widget.showHideText
            ? IconButton(
                icon: Icon(_hideText ? Icons.visibility : Icons.visibility_off),
                onPressed: () {
                  setState(() {
                    _hideText = !_hideText;
                  });
                },
              )
            : null,
      ),
      onChanged: widget.onChange,
    );
  }
}
