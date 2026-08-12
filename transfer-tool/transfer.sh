#!/usr/bin/env bash
#
# transfer.sh - Bash tool to upload and download files via free.keep.sh.
#
# Usage:
#   Upload:   ./transfer.sh <file1> [file2 ...]
#   Download: ./transfer.sh -d <directory> <file_id> <file_name>
#   Help:     ./transfer.sh -h
#   Version:  ./transfer.sh -v

set -u

readonly CURRENT_VERSION="0.0.1"
readonly BASE_URL="https://free.keep.sh"

# Uploads a single file to free.keep.sh.
#
# Globals:
#   response - set to the server's response.
#
# Arguments:
#   $1 - path to the local file to upload.
#   $2 - file name to use on the remote server.
httpSingleUpload() {
    response=$(curl --silent --upload-file "$1" "${BASE_URL}/$2") || {
        echo "Failure!"
        return 1
    }
}

# Prints the result of an upload.
#
# Globals:
#   response - the URL returned by the server.
printUploadResponse() {
    cat <<EOF
Transfer File URL: ${response}
EOF
}

# Uploads a single file.
#
# Arguments:
#   $1 - path to the local file.
singleUpload() {
    local file_path
    file_path="${1/#\~/$HOME}"

    if [[ ! -f "${file_path}" ]]; then
        echo "Error: invalid file path"
        return 1
    fi

    local file_name
    file_name=$(basename "${file_path}")

    echo "Uploading ${file_name}"

    httpSingleUpload "${file_path}" "${file_name}"
}

# Downloads a single file from free.keep.sh.
#
# Arguments:
#   $1 - destination directory.
#   $2 - remote file id.
#   $3 - file name.
singleDowload() {
    local dir="$1"
    local file_id="$2"
    local file_name="$3"

    mkdir -p "${dir}"

    echo "Downloading ${file_name}"

    curl --progress-bar \
        -o "${dir}/${file_name}" \
        "${BASE_URL}/${file_id}/${file_name}" || {
        echo "Failure!"
        return 1
    }
}

# Prints the result of a download.
printDownloadResponse() {
    echo "Success!"
}

# Prints the help message.
showHelp() {
    cat <<EOF
Description: Bash tool to transfer files from the command line.

Usage:
  -d <dir> <id> <file>  Download <file> into <dir>
  -h                     Show the help message and exit
  -v                     Get the tool version

Examples:
  ./transfer.sh test.txt
  ./transfer.sh test.txt test2.txt
  ./transfer.sh -d ./downloads Mij6ca test.txt
  ./transfer.sh -v
EOF
}

main() {
    if [[ $# -eq 0 ]]; then
        showHelp
        exit 1
    fi

    case "$1" in
        -h)
            showHelp
            ;;

        -v)
            echo "${CURRENT_VERSION}"
            ;;

        -d)
            if [[ $# -ne 4 ]]; then
                echo "Error: invalid download arguments"
                showHelp
                exit 1
            fi

            shift

            singleDowload "$1" "$2" "$3" || exit 1
            printDownloadResponse
            ;;

        *)
            for file in "$@"; do
                singleUpload "${file}" || exit 1
                printUploadResponse
            done
            ;;
    esac
}

main "$@"
