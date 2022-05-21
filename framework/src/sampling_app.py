import typer
import wavetable_utils
import sample_manipulation

app = typer.Typer()


"""
    Split loaded sample into "micro-samples".
    Each "micro-sample" gets saved into a given directory.
"""
@app.command()
def split_into_microsamples_magic(
    export_name: str,
    import_filepath: str,
):
    samples, samplerate = sample_manipulation.load_wavefile(import_filepath, mono=True)
    if not samples.any(): raise "Failed to load wavefile."
    
    micro_samples = sample_manipulation.split_wavefile_into_microsamples_magic(samples)
    if not micro_samples.any(): raise "Microsample split failed."

    sample_manipulation.write_microsamples(
        micro_samples,
        export_name,
        samplerate=samplerate
    )


@app.command()
def split_into_microsamples(
    export_name: str,
    import_filepath: str,
    sample_times: int = typer.Argument(4)
):
    samples, samplerate = sample_manipulation.load_wavefile(import_filepath, mono=True)
    if not samples.any(): raise "Failed to load wavefile."

    micro_samples = sample_manipulation.split_wavefile_into_microsamples(samples, split=sample_times)
    if not micro_samples.any(): raise "Microsample split failed."
    
    sample_manipulation.write_microsamples(
        micro_samples,
        export_name,
        samplerate=samplerate
    )


"""
    Process given sample (.wav) to wavetable.
    Splits it into slices by using zero crossings and picking .005% of total sampled zero crossings.
    Afterwards generates an wavetable image and process its contents to generate an unique SHA256 name.
    After all is done save the wavetable.
"""
@app.command()
def process_sample_to_wavetable(
    import_filepath = typer.Argument(None),
    export_directory = typer.Argument(None),
    visualize_wavetable: bool = True
):
    if not import_filepath: return
    if not export_directory: return

    wavetable = wavetable_utils.load_wavetable(import_filepath)
    if not wavetable: return

    wavetable_utils.process_wavetable(
        wavetable, 
        export_directory=export_directory, 
        visualize_wavetable=visualize_wavetable
    )