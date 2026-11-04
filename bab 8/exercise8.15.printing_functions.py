def print_models(unprinted_designs, completed_models):
    """Mensimulasikan pencetakan desain 3D."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Sedang mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang selesai dicetak."""
    print("\nModel berikut telah selesai dicetak:")
    for model in completed_models:
        print(f"- {model}")