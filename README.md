# mspayload

> Windows AV/AppLocker bypass via msbuild and nps.

## Usage

`python3 mspayload.py`

Run the script to create a `mspayload_nps.xml` file with the appropriated payload.

Upload it to the target and run: `msbuild.exe mspayload_nps.xml` to start the build, make sure to setup your listener beforehand.

If `msbuild.exe` is not available, use the absolute path: `C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe`

## Disclaimer

I'm not responsible for your actions, this is script is provided as-is, do not use for illegal purposes.

Based on [trustedsec's](https://github.com/trustedsec/nps_payload) implementation.

## License

Code released under the [MIT](LICENSE).
