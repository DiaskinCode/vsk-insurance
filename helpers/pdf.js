export function base64toPDF(data) {
  const bufferArray = base64ToArrayBuffer(data)
  const blobStore = new Blob([bufferArray], { type: 'application/pdf' })
  if (window.navigator && window.navigator.msSaveOrOpenBlob) {
    window.navigator.msSaveOrOpenBlob(blobStore)
    return
  }
  const dataLocal = window.URL.createObjectURL(blobStore)
  const link = document.createElement('a')
  document.body.appendChild(link)
  link.href = dataLocal
  link.download = 'file.pdf'
  link.click()
  window.URL.revokeObjectURL(dataLocal)
  link.remove()
}

export const base64ToArrayBuffer = (data) => {
  const bString = window.atob(data)
  const bLength = bString.length
  const bytes = new Uint8Array(bLength)
  for (let i = 0; i < bLength; i++) {
    const ascii = bString.charCodeAt(i)
    bytes[i] = ascii
  }
  return bytes
}

function downloadURL(data, fileName) {
  const a = document.createElement('a')
  a.href = data
  a.download = fileName
  document.body.appendChild(a)
  a.style = 'display: none'
  a.click()
  a.remove()
}

function openURL(data) {
  window.open(data, '_blank');
}

export const downloadBlob = function (data, fileName, mimeType) {
  const blob = new Blob([data], {
    type: mimeType,
  })
  const url = window.URL.createObjectURL(blob)
  downloadURL(url, fileName)
  setTimeout(function () {
    return window.URL.revokeObjectURL(url)
  }, 1000)
}

export const openBlob = function (data, fileName, mimeType) {
  const blob = new Blob([data], {
    type: mimeType,
  })
  const url = window.URL.createObjectURL(blob)
  openURL(url)
  setTimeout(function () {
    return window.URL.revokeObjectURL(url)
  }, 1000)
}
