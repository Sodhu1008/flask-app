app.get('/todo', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'todo.html'));
});
