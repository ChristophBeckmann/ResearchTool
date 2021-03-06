import logging
import tkinter as tk
from gui import gui_helpers as helper
from researchtool.summarization import build_summary

logger = logging.getLogger(__name__)


class GUISummarize(tk.Toplevel):
    """
    Class for create the main Form
    # With help from this side: https://www.pythontutorial.net/tkinter/tkinter-toplevel/
    and this forum with own created problem: https://www.python-forum.de/viewtopic.php?f=18&t=54087
    """
    def __init__(self, parent):
        """
        Constructor for GUISummarize class
        """
        super().__init__(parent)

        self_width = 1200
        self_height = 800

        center_x, center_y = helper.center_form(self, self_width, self_height)  # Get center coordinates
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool - Summarize")
        self.configure(bg="#EEEEEE")

        # *Build Canvas*

        canvas = tk.Canvas(
            self,
            bg="#EEEEEE",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_rectangle(
            600.0,
            0.0,
            1200.0,
            800.0,
            fill="#00ADB5",
            outline="")

        # Labels

        canvas.create_text(
            207.0,
            17.0,
            anchor="nw",
            text="Insert Text:",
            fill="#222831",
            font=("Roboto", 36 * -1)
        )

        canvas.create_text(
            752.0,
            17.0,
            anchor="nw",
            text="Summarized Text:",
            fill="#EEEEEE",
            font=("Roboto", 36 * -1)
        )

        canvas.create_text(
            202.0,
            731.0,
            anchor="nw",
            text="Top:",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        # TextAreas

        textarea_text = tk.Text(
            self,
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0
        )
        textarea_text.place(
            x=50.0,
            y=79.0,
            width=500.0,
            height=602.0
        )

        textarea_summarized = tk.Text(
            self,
            bd=0,
            fg="#222831",
            bg="#EEEEEE",
            highlightthickness=0
        )
        textarea_summarized.place(
            x=650.0,
            y=79.0,
            width=500.0,
            height=602.0
        )

        # Spinbox

        spinbox_top = tk.Spinbox(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
            from_=1,
            to=50,
        )
        spinbox_top.place(
            x=267.0,
            y=716.0,
            width=65.0,
            height=56.0
        )

        # *Buttons*

        # Summarize Text
        self.btn_image_summarize = tk.PhotoImage(
            file=helper.assets("btn_summarize.png")
        )
        # Lambda Function Tuples. 1) Delete Textarea 2) Insert summarized text from build_summary function
        btn_summarize = tk.Button(
            self,
            image=self.btn_image_summarize,
            command=lambda: (
                textarea_summarized.delete(1.0, tk.END),
                textarea_summarized.insert(
                    1.0,
                    ". ".join(
                        build_summary(
                            textarea_text.get(1.0, tk.END),
                            int(spinbox_top.get())
                        )
                    )
                )
            )
        )
        btn_summarize.place(
            x=350.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        # Pathpicker
        self.btn_image_pathpicker = tk.PhotoImage(
            file=helper.assets("btn_pathpicker.png")
        )
        btn_pathpicker = tk.Button(
            self,
            image=self.btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: helper.open_textfile(textarea_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=716.0,
            width=65.0,
            height=58.0
        )

        # Export summarized Text
        self.btn_image_export = tk.PhotoImage(
            file=helper.assets("btn_export.png")
        )
        btn_export = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: helper.export_textarea(textarea_summarized),
            relief="flat"
        )
        btn_export.place(
            x=948.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        # Close Window
        self.btn_image_back = tk.PhotoImage(
            file=helper.assets("btn_back.png")
        )
        btn_back = tk.Button(
            self,
            image=self.btn_image_back,
            command=lambda: helper.close_window(self)
        )
        btn_back.place(
            x=0.0,
            y=0.0,
            width=65.0,
            height=58.0
        )
    
        self.resizable(False, False)
