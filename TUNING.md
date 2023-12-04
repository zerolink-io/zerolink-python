# Fine-tuning

To fine-tune the reasoning engine your ZeroLink Enterprise deployment must have
an attached `a2-ultragpu-8g` or `p4d.24xlarge` instance. The world graph
checkpoint hash must be passed and must validate against the model on the
server.

```python
% zerolink fine-tune create training_file.jsonl
```

The data format for `training_file.jsonl` must be newline-seperated file with
each line of the following schema.

```json
{
    "question": "",
    "answer": "",
    "nql": "",
    "plan": "",
    "proof": ""
}
```

`nql` must have a valid parse tree. Both `plan` and `proof` must validate as
valid JSON in the planning and proof schemas. Both will be normalized in
pre-processing to compute the CodeBLEU metrics.
