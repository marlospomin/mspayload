# mspayload

> Windows AV/AppLocker bypass via msbuild.

## Usage

`python3 mspayload.py`

Run the script to create a `mspayload_nps.xml` file with the appropriated payload. (Only reverse_tcp is available at this time.)

Upload it to the target and run `C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe mspayload_nps.xml` to start the build, make sure to setup your listener before running the command.

Compatible with `meterpreter` payloads.

## Disclaimer

I'm not responsible for your actions, this is script is provided as-is, do not use for illegal purposes.

Based on [trustedsec's](https://github.com/trustedsec/nps_payload) implementation.

## TODO

* Add a better/cleaner payload.
* Add some sort of argument parsing.
* Add more options.
* Refactor the code.

## License

Code released under the [MIT](LICENSE).
