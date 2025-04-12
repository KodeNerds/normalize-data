import { useState } from 'react'

function App() {
  const [fileList, setFileList] = useState([]);
  const [downloadUrl, setDownloadUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFileList(e.target.files);
  };

  const handleUpload = async () => {
    if (!fileList.length) return;
    const formData = new FormData();
    for (let file of fileList) {
      formData.append("files", file);
    }

    setLoading(true);
    try {
      const res = await fetch("/api/normalize", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setDownloadUrl(data.downloadUrl);
    } catch (err) {
      alert("Upload failed.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-lg w-full text-center">
        <h1 className="text-2xl font-bold mb-4">Jewelry Data Normalizer</h1>
        <input
          type="file"
          multiple
          onChange={handleFileChange}
          className="mb-4 block w-full text-sm text-gray-700"
        />
        <button
          onClick={handleUpload}
          disabled={loading}
          className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded"
        >
          {loading ? "Uploading..." : "Normalize & Upload"}
        </button>
        {downloadUrl && (
          <div className="mt-4">
            <a
              href={downloadUrl}
              download
              className="text-blue-600 underline"
            >
              Download Normalized CSV
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
