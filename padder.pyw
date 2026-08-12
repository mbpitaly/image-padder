import os
import time
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image

def pad_photos():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select Photos to Pad",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
    )

    if not file_paths:
        return

    # --- Settings Popup ---
    target_ratio_val = None
    output_dir_val = None

    def submit_settings():
        nonlocal target_ratio_val, output_dir_val
        sel = ratio_var.get()
        num, den = sel.split(':')
        val = float(num) / float(den)
        
        if vertical_var.get():
            target_ratio_val = 1.0 / val
        else:
            target_ratio_val = val
            
        output_dir_val = out_dir_var.get()
        ratio_win.destroy()

    def browse_out_dir():
        # Drop topmost status temporarily so the folder explorer can actually be seen
        ratio_win.attributes('-topmost', False)
        
        d = filedialog.askdirectory(
            parent=ratio_win,
            title="Select Base Folder",
            initialdir=os.path.dirname(out_dir_var.get())
        )
        
        # Bring topmost status back
        ratio_win.attributes('-topmost', True)
        
        if d:
            out_dir_var.set(os.path.join(d, "Padded"))

    ratio_win = tk.Toplevel(root)
    ratio_win.title("Padding Settings")
    ratio_win.resizable(False, False)
    ratio_win.attributes('-topmost', True) 
    
    # Aspect Ratio Row
    tk.Label(ratio_win, text="Aspect Ratio:").grid(row=0, column=0, padx=(15,5), pady=(15,5), sticky="e")
    
    ratio_var = tk.StringVar(value="5:4")
    # Added 1:1 and 1.91:1 right here:
    ratio_options = ["1:1", "3:2", "4:3", "5:4", "1.91:1", "2.4:1", "16:9"]
    ratio_cb = ttk.Combobox(ratio_win, textvariable=ratio_var, values=ratio_options, state="readonly", width=8)
    ratio_cb.grid(row=0, column=1, padx=5, pady=(15,5), sticky="w")
    
    vertical_var = tk.BooleanVar(value=False)
    vertical_chk = ttk.Checkbutton(ratio_win, text="Vertical", variable=vertical_var)
    vertical_chk.grid(row=0, column=2, padx=5, pady=(15,5), sticky="w")
    
    # Output Folder Row
    tk.Label(ratio_win, text="Save To:").grid(row=1, column=0, padx=(15,5), pady=5, sticky="e")
    
    default_out = os.path.join(os.path.expanduser("~"), "Desktop", "Padded")
    out_dir_var = tk.StringVar(value=default_out)
    out_entry = ttk.Entry(ratio_win, textvariable=out_dir_var, width=30)
    out_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")
    
    ttk.Button(ratio_win, text="Browse...", command=browse_out_dir).grid(row=1, column=3, padx=(5,15), pady=5)
    
    # Submit Button
    ttk.Button(ratio_win, text="Start Padding", command=submit_settings).grid(row=2, column=0, columnspan=4, pady=(15, 15))
    
    # Center the popup
    ratio_win.update_idletasks()
    x = (ratio_win.winfo_screenwidth() // 2) - (ratio_win.winfo_width() // 2)
    y = (ratio_win.winfo_screenheight() // 2) - (ratio_win.winfo_height() // 2)
    ratio_win.geometry(f"+{x}+{y}")
    
    root.wait_window(ratio_win)

    # Abort if user closed the window instead of clicking Start
    if target_ratio_val is None or not output_dir_val:
        root.destroy()
        return
    # ------------------------------------

    os.makedirs(output_dir_val, exist_ok=True)

    border_percent = 0.05
    max_pixels = 6000000
    total_files = len(file_paths)

    prog_win = tk.Toplevel(root)
    prog_win.title("Processing Photos")
    prog_win.geometry("300x100")
    prog_win.resizable(False, False)

    lbl = tk.Label(prog_win, text=f"Padding 0 of {total_files} photos...")
    lbl.pack(pady=10)

    progress = ttk.Progressbar(prog_win, orient="horizontal", length=250, mode="determinate")
    progress.pack(pady=5)
    progress["maximum"] = total_files

    prog_win.update()

    for i, filepath in enumerate(file_paths):
        filename = os.path.basename(filepath)

        try:
            with Image.open(filepath) as img:
                exif = img.getexif()
                
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')

                w, h = img.size

                if w * h > max_pixels:
                    scale = (max_pixels / (w * h)) ** 0.5
                    w = int(w * scale)
                    h = int(h * scale)
                    img = img.resize((w, h), Image.Resampling.LANCZOS)

                target_ratio = target_ratio_val

                border_px = int(max(w, h) * border_percent)

                virt_w = w + (border_px * 2)
                virt_h = h + (border_px * 2)
                virt_ratio = virt_w / virt_h

                if virt_ratio > target_ratio:
                    canvas_w = virt_w
                    canvas_h = int(virt_w / target_ratio)
                else:
                    canvas_h = virt_h
                    canvas_w = int(virt_h * target_ratio)

                padded_img = Image.new('RGB', (canvas_w, canvas_h), 'white')

                offset_x = (canvas_w - w) // 2
                offset_y = (canvas_h - h) // 2
                padded_img.paste(img, (offset_x, offset_y))

                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_padded{ext}"
                new_filepath = os.path.join(output_dir_val, new_filename)

                padded_img.save(new_filepath, quality=85, exif=exif)

        except Exception:
            pass

        progress["value"] = i + 1
        lbl.config(text=f"Padding {i + 1} of {total_files} photos...")
        prog_win.update()

    # --- 1 Second Wait Sequence ---
    lbl.config(text="Done!")
    prog_win.update()

    # Polls for 1 second (10 * 0.1s)
    try:
        for _ in range(10):
            prog_win.update()
            time.sleep(0.1)
    except tk.TclError:
        pass

    root.destroy()

if __name__ == "__main__":
    pad_photos()