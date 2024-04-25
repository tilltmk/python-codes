<p>Clipboard Changed: def monitor<em>activities(self):
    previous</em>clipboard = ""
    previous_window = None</p>

<pre><code>while self.is_running:
    # Capture clipboard content
    current_clipboard = clipboard.paste()
    if current_clipboard != previous_clipboard:
        self.markdown_log += f"\nClipboard Changed: {current_clipboard}"
        previous_clipboard = current_clipboard

    # Capture active window
    active_window = gw.getActiveWindow()
    if active_window and (active_window != previous_window):
        self.markdown_log += f"\nWindow Selected: {active_window.title}"
        screenshot = ImageGrab.grab(bbox=active_window.box)
        screenshot.save(f"{time.time()}_screenshot.png")
        previous_window = active_window

    # Capture typed keys (corrected version)
    key_events = keyboard.record(until='enter')
    typed_text = ''.join([event.name for event in key_events if event.event_type == 'down'])
    self.text_buffer += typed_text
    self.markdown_log += f"\nTyped Text: {self.text_buffer}"
    self.text_buffer = ""

    time.sleep(1)  # Reduce CPU usage
</code></pre>

<p>Window Selected: Activity Monitor
Typed Text: tstbackspacebackspaceestenter
Window Selected: Hyper
Typed Text: tnach-rechtsenter
Typed Text: test.de+backspaceenter
Window Selected: Stiftung Warentest | Unabh�ngig. Objektiv. Unbestechlich. � Mozilla Firefox</p>
